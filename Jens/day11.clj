(defn parse-row [y row]
  (let [coords (map-indexed (fn [x _] [x y]) row)]
    (as-> coords $
      (filter #(= \L (nth row (first %))) $)
      (zipmap $ (repeat \L)))))

(def input (let [raw (clojure.string/split-lines (slurp "inputs/day11.txt"))]
             (->> raw
                  (map #(map identity %))
                  (map-indexed parse-row)
                  (apply merge)
                  (#(assoc % :height (count raw) :width (count (first raw)))))))

(defn occupied? [layout coord]
  (condp = (get layout coord)
    \# true
    false))

(defn adjacent [layout [x y]]
  (let [seats [[(dec x) (dec y)] [(dec x) y] [(dec x) (inc y)] [x (dec y)]
               [x (inc y)] [(inc x) (dec y)] [(inc x) y] [(inc x) (inc y)]]]
    (map #(get layout %) seats)))

(defn adjacent-occupied [layout coord]
  (filter #(= \# %) (adjacent layout coord)))

(defn first-visible [layout [x y] [dx dy]]
  (loop [[cx cy] [(+ x dx) (+ y dy)]]
    (if (or (< cx 0) (> cx (:width layout))
            (< cy 0) (> cy (:height layout)))
      nil
      (if-let [seat (get layout [cx cy])]
        seat
        (recur [(+ cx dx) (+ cy dy)])))))

(defn visible-occupied [layout coord]
  (let [dirs [[-1 -1] [-1 0] [-1 1] [0 -1] [0 1] [1 -1] [1 0] [1 1]]]
    (filter #(= \# %) (map #(first-visible layout %1 %2) (repeat coord) dirs))))

(defn update-seat [layout coord threshold spotting-fn]
  (cond
    (and (occupied? layout coord)
         (<= threshold (count (spotting-fn layout coord))))
    [coord \L]
    (and (not (occupied? layout coord))
         (zero? (count (spotting-fn layout coord))))
    [coord \#]
    :else [coord (get layout coord)]))

(defn print-layout [layout]
  (map-indexed (fn [y row]
                 (apply str
                        (map-indexed (fn [x _]
                                       (if-let [s (get layout [x y])]
                                         s
                                         \.)) row))) (repeat 10 (repeat 10 []))))

(defn step [layout spotting-fn threshold]
  (do (print-layout layout)
    (->> (keys layout)
         (remove keyword?)
         (mapcat #(update-seat layout % threshold spotting-fn))
         (apply hash-map)
         (#(assoc % :width (:width layout) :height (:height layout))))))

(defn reach-steady-state [layout spotting-fn threshold]
  (reduce #(if (= %1 %2) (reduced %1) %2) (iterate #(step % spotting-fn threshold) layout)))

(defn day11-1 [in]
  (->> (reach-steady-state in adjacent-occupied 4)
       (map #(filter (partial = \#) %))
       (map count)
       (reduce +)))

(println (str "Part one: " (day11-1 input)))

(defn day11-2 [in]
  (->> (reach-steady-state in visible-occupied 5)
       (map #(filter (partial = \#) %))
       (map count)
       (reduce +)))

(println (str "Part two: " (day11-2 input)))
