(def input (->> "inputs/day01.txt"
                slurp
                clojure.string/split-lines
                (map #(Integer/parseInt %))))

(defn sum-two-to [s lst]
  (let [threshold  (/ s 2)
        [low high] (split-with (partial > threshold) (sort lst))]
    (if (or (empty? low) (empty? high))
      nil
      (loop [l low
             h (reverse high)]
        (cond
          (empty? l) nil
          (empty? h)
          (if (<= 2 (count (take-while (partial = threshold) (reverse low))))
            [threshold threshold]
            nil)
          (= s (+ (first l) (first h))) [(first l) (first h)]
          (< s (+ (first l) (first h))) (recur low
                                               (drop 1 h))
          :else                         (recur (drop 1 l)
                                               h))))))

(defn day1-1 []
  (apply * (sum-two-to 2020 input)))

(defn day1-2 []
  (loop [lst input]
    (if-let [res (sum-two-to (- 2020 (first lst)) (drop 1 lst))]
      (reduce * (first lst) res)
      (recur (drop 1 lst)))))
