(def input (let [raw (clojure.string/split-lines (slurp "inputs/day17.txt"))]
             (set (for [x (range 0 (count (first raw)))
                        y (range 0 (count raw))
                        :when (= \# (nth (nth raw y) x))]
                    [x y 0]))))

(defn neighbours
  ([coords]
   (loop [lower-d-coords (map vector (range (dec (first coords)) (+ 2 (first coords))))
          higher-d-coords (next coords)]
     (if (empty? higher-d-coords)
       (disj (set lower-d-coords) coords)
       (recur (for [l lower-d-coords
                    h (range (dec (first higher-d-coords)) (+ 2 (first higher-d-coords)))]
                (conj l h))
              (next higher-d-coords))))))

(defn active? [state coord]
  (contains? state coord))

(defn active-neighbours [old-state coord]
  (filter true? (map #(active? old-state %) (neighbours coord))))

(defn survival [old-state coord]
  (let [an (count (active-neighbours old-state coord))]
    (if (or (and (active? old-state coord) (<= 2 an 3))
            (and (not (active? old-state coord)) (= 3 an)))
      coord
      nil)))

(defn step [old-state]
  (set (filter some? (map survival (repeat old-state)
                          (clojure.set/union old-state (mapcat neighbours old-state))))))

(defn day17 [initial-state]
  (count (nth (iterate step initial-state) 6)))

(println (str "Part one: There are " (day17 input) " active cells after 6 cycles"))

(def input2 (set (map conj input (repeat 0))))

(println (str "Part two: There are " (day17 input2) " active cells after 6 cycles"))
