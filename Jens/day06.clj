(def input (->> "inputs/day06.txt"
                slurp
                (re-seq #"(?<=^|\n\n)(?:[a-z]+\n{0,1})+")))

(defn day6-1 []
  (->> input
       (map #(clojure.string/replace % #"\n" ""))
       (map set)
       (map count)
       (reduce +)))

(defn find-common [ans]
  (apply clojure.set/intersection (map set ans)))

(defn day6-2 []
  (->> input
       (map clojure.string/split-lines)
       (map find-common)
       (map count)
       (reduce +)))
