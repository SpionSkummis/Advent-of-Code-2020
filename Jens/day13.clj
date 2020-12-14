(def input (->> "inputs/day13.txt"
                slurp
                (re-seq #"[\dx]+")
                (map #(if (not= "x" %) (Integer/parseInt %) %))))

(defn waiting-time [bus-id time]
  (- (* bus-id (inc (quot time bus-id))) time))

(defn day13-1 [in]
  (apply * (first (sort-by second (map #(vector % (waiting-time % (first in)))
                                       (remove (partial = "x") (next in)))))))

(println (str "Part one: " (day13-1 input)))

(defn get-mod [bus]
  (mod (- (last bus) (first bus)) (last bus)))

(defn euclid [x y]
  (if (zero? (mod x y))
    [0 1 y]
    (let [[a b r] (euclid y (mod x y))]
      [b (- a (* (quot x y) b))  r])))

(defn inv [n modulus]
  (mod (+ (second (euclid modulus (mod n modulus))) modulus) modulus))

(defn chinese-remainder [coeffs mods]
  (let [m  (reduce * mods)
        Ms (map #(/ m %) mods)
        xs (map inv Ms mods)]
    (mod (reduce + (map * coeffs Ms xs)) m)))

(defn day13-2 [in]
  (->> (map-indexed vector (next input))
       (remove #(= "x" (last %)))
       (map #(vector (- (last %) (first %)) (last %)))
       (#(chinese-remainder (map first %) (map last %)))))

(println (str "Part two: " (day13-2 input)))
