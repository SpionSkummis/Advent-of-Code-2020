(def input (->> "inputs/day05.txt"
                slurp
                (re-seq #"[BF]{7}[LR]{3}")))



(defn find-seat [s]
  (loop [rem s
         row (range 128)
         col (range 8)]
    (condp = (first rem)
      nil [(first row) (first col)]
      \B  (recur (next rem) (drop (/ (count row) 2) row) col)
      \F  (recur (next rem) (take (/ (count row) 2) row) col)
      \L  (recur (next rem) row (take (/ (count col) 2) col))
      \R  (recur (next rem) row (drop (/ (count col) 2) col)))))

(defn seat-id [[row col]]
  (+ (* 8 row) col))

(defn day5-1 []
  (->> input
       (map find-seat)
       (map seat-id)
       (reduce max)))

(defn find-missing [a b]
  (if (= (inc a) b)
    b
    (reduced (inc a))))

(defn day5-2 []
  (->> input
       (map find-seat)
       (map seat-id)
       sort
       (reduce find-missing)))
