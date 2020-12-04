(def input (->> "inputs/day03.txt"
                slurp
                clojure.string/split-lines))

(def pattern-height (count input))
(def pattern-width (count (first input)))

(defn tree-at? [[x y]]
  (= \# (nth (nth input y) x)))

(defn count-trees-in-path [slope]
  (loop [pos [0 0]
         trees 0]
    (if (>= (last pos) pattern-height)
      trees
      (recur (update-in (mapv + pos slope)
                        [0] #(mod % pattern-width))
             (if (tree-at? pos)
               (inc trees)
               trees)))))

(defn day3-1 []
  (count-trees-in-path [3 1]))

(def slopes [[1 1] [3 1] [5 1] [7 1] [1 2]])

(defn day3-2 []
  (->> slopes
       (map count-trees-in-path)
       (apply *)))
