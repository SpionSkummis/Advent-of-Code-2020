(def input (clojure.string/split-lines (slurp "inputs/day14.txt")))

(defn mask [s]
  {:and (Long/parseLong (clojure.string/replace s #"X" "1") 2)
   :or (Long/parseLong (clojure.string/replace s #"X" "0") 2)
   :raw s})

(defn apply-mask [number msk mode]
  (case mode
    1 (-> number
          (bit-and (:and msk))
          (bit-or (:or msk)))
    2 (loop [i 0
               o #{(bit-or number (:or msk))}]
          (if-let [j (clojure.string/index-of (clojure.string/reverse (:raw msk)) \X i)]
            (recur (inc j) (into o (mapcat (fn [f] (map #(f % j) o)) [bit-set bit-clear])))
            o))))

(defn exec-line [line msk mem mode]
  (if (re-find #"mask" line)
    [(mask (re-find #"[X10]+" line)) mem]
    (let [[_ i v] (re-find #"mem\[(\d+)\] = ([\d]+)" line)]
      (case mode
        1 [msk (assoc-in mem [(Long/parseLong i)] (apply-mask (Long/parseLong v) msk mode))]
        2 [msk (merge mem (apply hash-map (mapcat vector
                                                  (apply-mask (Long/parseLong i) msk mode)
                                                  (repeat (Long/parseLong v)))))]))))

(defn run-program [prog mode]
  (loop [msk (mask (re-find #"[X10]+" (first prog)))
         prg (next prog)
         mem {}]
    (if (empty? prg)
      mem
      (let [[new-msk new-mem] (exec-line (first prg) msk mem mode)]
        (recur new-msk (next prg) new-mem)))))

(defn day14-1 [in]
  (apply + (vals (run-program in 1))))

(println (str "Part one: " (day14-1 input)))

(defn day14-2 [in]
  (apply + (vals (run-program in 2))))

(println (str "Part two: " (day14-2 input)))
