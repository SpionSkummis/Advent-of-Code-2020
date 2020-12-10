(def input (->> "inputs/day10.txt"
                slurp
                clojure.string/split-lines
                (map #(Integer/parseInt %))))

(defn count-differences [a b]
  (let [diff (- b (:last a))]
    (-> a
        (update-in [diff] inc)
        (assoc-in [:last] b))))

(defn day10-1 [in]
  (let [chain (reduce count-differences {1 0 2 0 3 0 :last 0} (sort in))]
    (* (get chain 1) (inc (get chain 3)))))

(println (str "Part 1: " (day10-1 input)))

(def ways-to-the-top
  (memoize (fn [x lst]
             (let [larger (drop-while #(< (+ x 3) %) (take-while #(< x %) lst))]
               (if (empty? larger)
                 1
                 (reduce + (map #(ways-to-the-top % lst) larger)))))))

(defn day10-2 [in]
  (let [lst (sort > (conj in 0))]
    (last (map #(ways-to-the-top % lst) lst))))

(println (str "Part 2: " (day10-2 input)))
