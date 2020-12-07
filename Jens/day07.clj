(defn parse-rule [[_ outer contents]]
  (let [cont    (re-seq #"(\d+) ([a-z]+ [a-z]+) bag[s]{0,1}" contents)
        amounts (map #(Integer/parseInt (second %)) cont)
        types   (map #(nth % 2) cont)]
    {outer (apply merge (map hash-map types amounts))}))

(def rules (->> "inputs/day07.txt"
                slurp
                (re-seq #"([a-z]+\s[a-z]+) bags contain (.+)")
                (map parse-rule)
                (apply merge)))

(defn contained-in [bag]
  (letfn [(has-key? [x k] (some #(= k %) (keys x)))]
    (filter #(has-key? (second %) bag) rules)))

(defn find-ancestors [x]
  (loop [looking-for [x]
         found       #{}]
    (if (empty? looking-for)
      found
      (let [new (map first (contained-in (first looking-for)))]
        (recur (into (next looking-for) new)
               (into found new))))))

(defn day7-1 []
  (count (find-ancestors "shiny gold")))

(def bag-count
  (memoize (fn [x]
             (if-let [bag (rules x)]
               (reduce + 1 (map #(* (bag-count %1) %2) (keys bag) (vals bag)))
               1))))

(defn day7-2 []
  (dec (bag-count "shiny gold")))
