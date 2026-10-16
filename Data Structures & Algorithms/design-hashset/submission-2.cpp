class MyHashSet {

private:
    std::unordered_map<int, std::list<int>> hashmap;
    int hashNum{10000};
public:
    MyHashSet() {
    }
    
    void add(int key) {
        if (contains(key)){
            return;
        }
        int hashed_num{key % hashNum};
        hashmap[hashed_num].push_back(key);
    }
    
    void remove(int key) {
        int hashed_num{key % hashNum};
        auto bucket = hashmap.find(hashed_num);
        if (bucket == hashmap.end()){
            return;
        }

        auto& linkedList = bucket->second; 
        auto it = std::find(linkedList.begin(), linkedList.end(), key);
        if (it != linkedList.end()){
            linkedList.erase(it);
        }

    }
    
    bool contains(int key) {
        int hashed_num{key % hashNum};
        auto bucket = hashmap.find(hashed_num);
        if (bucket == hashmap.end()){
            return false;
        }

        auto linkedList = bucket->second; // we get the hashmap
        return std::find(linkedList.begin(), linkedList.end(), key) != linkedList.end();
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */