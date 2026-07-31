/*
we have a linked list of frequency buckets
each of these buckets contains a linked list of actual entries in the cache
an unordered map points to these nodes and also contains the node's frequency

when we get, we index into the map to get the node ptr and frequency. we then
remove the node from the list, increment the frequency, and insert it into the next
frequency bucket. if no bucket exists, allocate one.

when we put, if the node exists we do the exact same thing and update the node's value. if it doesn't we allocate a new node in the 1 freq bucket, and if that doesn't
exist we create it. if the size == capacity, we remove the node from its bucket. if
the node's bucket is now empty, then we remove that bucket as well.

*/

class LFUCache {
public:
    LFUCache(int capacity) : cap_{capacity} {}
    
    int get(int key) {
        auto node_itr{nodes_.find(key)};
        if (node_itr == nodes_.end()) {
            return -1;
        }

        increase_frequency_(key, node_itr->second);
        return node_itr->second.value;
    }

    void put(int key, int value) {
        if (cap_ == 0) {
            return;
        }

        auto node_itr{nodes_.find(key)};

        if (node_itr != nodes_.end()) {
            node_itr->second.value = value;
            increase_frequency_(key, node_itr->second);
            return;
        }

        if (nodes_.size() == static_cast<std::size_t>(cap_)) {
            auto& bucket{buckets_[min_frequency_]};

            int key_to_remove{bucket.back()};
            bucket.pop_back();

            if (bucket.empty()) {
                buckets_.erase(min_frequency_);
            }

            nodes_.erase(key_to_remove);
        }

        min_frequency_ = 1;

        auto& bucket{buckets_[1]};
        bucket.push_front(key);

        nodes_.emplace(
            key,
            Node{
                .value = value,
                .frequency = 1,
                .position = bucket.begin()
            }
        );
    }
private:
    struct Node {
        int value;
        int frequency;
        std::list<int>::iterator position;
    };

    std::unordered_map<int, std::list<int>> buckets_;
    std::unordered_map<int, Node> nodes_;

    int cap_;
    int min_frequency_{};

    void increase_frequency_(int key, Node& node) {
        int old_frequency{node.frequency};
        auto& old_bucket{buckets_[old_frequency]};

        old_bucket.erase(node.position);

        if (old_bucket.empty()) {
            buckets_.erase(old_frequency);

            if (min_frequency_ == old_frequency) {
                ++min_frequency_;
            }
        }

        ++node.frequency;

        auto& new_bucket{buckets_[node.frequency]};
        new_bucket.push_front(key);
        node.position = new_bucket.begin();
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */