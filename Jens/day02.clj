(def input (->> "inputs/day02.txt"
                slurp
                (re-seq #"(\d+)\-(\d+)\s([a-z])\:\s*([a-z]+)")))

(defn valid-password? [pw ch lower upper]
  (let [c (count (re-seq (re-pattern ch) pw))]
    (<= lower c upper)))

(defn day2-1 []
  (->> input
       (map #(valid-password? (last %) (nth % 3)
                             (Integer/parseInt (nth % 1))
                             (Integer/parseInt (nth % 2))))
       (filter true?)
       count))

(defn valid-password2? [pw ch i1 i2]
  (let [chars [(nth pw (dec i1))
               (nth pw (dec i2))]
        c (count (filter #(= (first ch) %) chars))]
    (= c 1)))

(defn day2-2 []
  (->> input
       (map #(valid-password2? (last %) (nth % 3)
                             (Integer/parseInt (nth % 1))
                             (Integer/parseInt (nth % 2))))
       (filter true?)
       count))
