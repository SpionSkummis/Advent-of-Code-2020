(def input (->> "inputs/day11.txt"
                slurp
                clojure.string/split-lines
                (map #(map identity %))))

(def layout-height (count input))
(def layout-width (count (first input)))

(defn get-seat [layout [^Integer x ^Integer y]]
  (nth (nth layout y) x))

(defn occupied? [layout coord]
  (condp = (get-seat layout coord)
    \# true
    false))

(defn adjacent [layout [^Integer x ^Integer y]]
  (remove #(or (< (first %) 0)
               (< (second %) 0)
               (>= (first %) layout-width)
               (>= (second %) layout-height))
          [[(dec x) y] [(dec x) (dec y)] [(dec x) (inc y)]
           [(inc x) y] [(inc x) (dec y)] [(inc x) (inc y)]
           [x (dec y)] [x (inc y)]]))

(defn adjacent-occupied [layout coord]
  (filter #(occupied? layout %) (adjacent layout coord)))

(defn update-seat [layout coord]
  (cond
    (= \. (get-seat layout coord)) \.
    (and (occupied? layout coord)
         (<= 4 (count (adjacent-occupied layout coord)))) \L
    (and (not (occupied? layout coord))
         (zero? (count (adjacent-occupied layout coord)))) \#
    :else (get-seat layout coord)))

(defn step [layout]
  (map-indexed (fn [y r] (map-indexed (fn [x s] (update-seat layout [x y]))
                                      r))
               layout))

(defn reach-steady-state [layout]
  (reduce #(if (= %1 %2) (reduced %1) %2) (iterate step layout)))

(defn day11-1 [in]
  (->> (reach-steady-state in)
       (map #(filter (partial = \#) %))
       (map count)
       (reduce +)))
