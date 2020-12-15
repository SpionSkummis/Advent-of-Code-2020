(def input [14 8 16 0 1 17])

(def initial-game {:turn (count input)
                   :word (last input)
                   :spoken (apply hash-map (mapcat vector (drop-last input) (next (range))))})

(defn speak-word [game]
  (let [word (if-let [p (get (:spoken game) (:word game))]
               (- (:turn game) p)
               0)]
    (-> game
        (assoc-in [:spoken (:word game)] (:turn game))
        (assoc-in [:word] word)
        (update-in [:turn] inc))))

(defn nth-game [start-game n]
  (->> start-game
       (iterate speak-word)
       (drop (- n (:turn start-game)))
       first))

(defn day15-1 [in]
  (:word (nth-game in 2020)))

(println (str "Part one: The 2020th word spoken is " (day15-1 initial-game)))

(defn day15-2 [in]
  (:word (nth-game in 30000000)))

(println (str "Part two: 30 000 000 isn't that big of a number. The word is " (day15-2 initial-game)))
