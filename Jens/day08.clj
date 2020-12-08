(def input (->> "inputs/day08.txt"
                slurp
                (re-seq #"([a-z]{3}) ([+-]\d+)")
                (map next)
                (map #(vector (first %) (Integer/parseInt (second %))))
                (into [])))

(defn exec-line [p i]
  (let [inst (first (nth (:code p) i))
        v    (second (nth (:code p) i))]
    (-> (condp = inst
          "nop" p
          "acc" (update-in p [:accumulator] #(+ % v))
          "jmp" (update-in p [:index] #(+ % (dec v))))
        (update-in [:index] inc))))

(defn program [code]
  {:index       0
   :accumulator 0
   :code        code})

(defn run-code [prog]
  (loop [seen #{}
         p    prog]
    (cond
      (contains? seen (:index p))       [false (:accumulator p)]
      (>= (:index p) (count (:code p))) [true (:accumulator p)]
      :else                             (recur (conj seen (:index p))
                                               (exec-line p (:index p))))))

(defn day8-1 []
  (run-code (program input)))

(defn flip-inst [p n]
  (loop [n n
         i 0]
    (if (zero? n)
      (condp = (first (nth (:code p) i))
        "nop" (assoc-in p [:code i 0] "jmp")
        "jmp" (assoc-in p [:code i 0] "nop")
        (recur n (inc i)))
      (condp = (first (nth (:code p) i))
        "acc" (recur n (inc i))
        (recur (dec n) (inc i))))))

(defn day8-2 []
  (let [def-prog (program input)]
    (loop [i 0
           p def-prog]
      (let [res (run-code p)]
        (if (true? (first res))
          (second res)
          (recur (inc i)
                 (flip-inst def-prog i)))))))
