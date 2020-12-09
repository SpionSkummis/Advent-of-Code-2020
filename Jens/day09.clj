(def input (->> "inputs/day09.txt"
                slurp
                clojure.string/split-lines
                (map #(Long/parseLong %))))

;; Reusing day 1, what a joy!
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

(defn day9-1 [in]
  (loop [[window remaining] (map #(into [] %) (split-at 5 in))]
    (if (sum-two-to (first remaining) window)
      (recur [(conj (subvec window 1) (first remaining))
              (next remaining)])
      (first remaining))))

(defn sum-from-start [s l]
  #dbg (loop [sum 0
         lst l
         i   0]
    (cond
      (= s sum) (take i l)
      (< s sum) nil
      :else     (recur (+ sum (first lst))
                       (next lst)
                       (inc i)))))

(defn day9-2 [in]
  (let [invalid (day9-1 in)]
    (loop [lst in]
      (if-let [rng (sum-from-start invalid lst)]
        (+ (apply min rng) (apply max rng))
        (recur (next lst))))))
