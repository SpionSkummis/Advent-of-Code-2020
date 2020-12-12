(def input (->> "inputs/day12.txt"
                slurp
                (re-seq #"([NSEWFLR])(\d+)")
                (map #(vector (second %) (Integer/parseInt (last %))))))

(defn make-ship [instruction-set]
  {:x 0, :y 0, :facing 0, :instructions instruction-set})

(defn to-dir [n]
  (get {0 "E", 90 "N", 180 "W", 270 "S"} (mod n 360)))

(defn move [thing dir dist]
  (case dir
    "N" (update-in thing [:y] + dist)
    "S" (update-in thing [:y] - dist)
    "E" (update-in thing [:x] + dist)
    "W" (update-in thing [:x] - dist)
    "F" (move thing (to-dir (:facing thing)) dist)))

(defn run-instruction [ship inst]
  (case (first inst)  
    "L" (update-in ship [:facing] + (second inst))
    "R" (update-in ship [:facing] - (second inst))
    (move ship (first inst) (second inst))))

(defn step [ship]
  (-> ship
      (run-instruction (first (:instructions ship)))
      (update-in [:instructions] next)))

(defn day12-1 [in]
  (loop [ship (make-ship in)]
    (if (empty? (:instructions ship))
      (+ (Math/abs (:x ship)) (Math/abs (:y ship)))
      (recur (step ship)))))

(defn make-ship2 [instruction-set]
  {:x 0, :y 0, :waypoint {:x 10, :y 1}, :instructions instruction-set})

(defn move-ship2 [ship]
  (-> ship
      (update-in [:x] + (:x (:waypoint ship)))
      (update-in [:y] + (:y (:waypoint ship)))))

(defn rotate-waypoint [wp dir dist]
  (case dir
    "R" (rotate-waypoint wp "L" (- 360 dist))
    "L" (let [new-coords (condp = (mod dist 360)
                           0   {:x (:x wp), :y (:y wp)}
                           90  {:x (- (:y wp)), :y (:x wp)}
                           180 {:x (- (:x wp)), :y (- (:y wp))}
                           270 {:x (:y wp), :y (- (:x wp))})]
          (merge wp new-coords))))

(defn run-instruction2 [ship inst]
  (case (first inst)
    ("L" "R") (update-in ship [:waypoint] rotate-waypoint (first inst) (last inst))
    ("N" "S" "E" "W") (update-in ship [:waypoint] move (first inst) (last inst))
    ("F") (nth (iterate move-ship2 ship) (last inst))))

(defn step2 [ship]
  (-> ship
      (run-instruction2 (first (:instructions ship)))
      (update-in [:instructions] next)))

(defn day12-2 [in]
  (loop [ship (make-ship2 in)]
    (if (empty? (:instructions ship))
      (+ (Math/abs (:x ship)) (Math/abs (:y ship)))
      (recur (step2 ship)))))
