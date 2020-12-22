(def input (clojure.string/split-lines (slurp "inputs/day18.txt")))

(defn next-paren-ids [s]
  (loop [i   0
         lst 0
         st  s]
    (cond
      (empty? st)       nil
      (= \( (first st)) (recur (inc i) i (next st))
      (= \) (first st)) [lst (inc i)]
      :else (recur (inc i) lst (next st)))))

(defn remove-parens [s mode]
  (loop [p  (count (re-seq #"\(" s))
         st s]
    (if (zero? p)
      st
      (let [[l r] (next-paren-ids st)]
        (recur (dec p)
               (str (subs st 0 l)
                    (eval-str (subs st (inc l) r) mode)
                    (subs st r)))))))

(defn to-pairwise [lst]
  (loop [l (next lst)
         o [(first lst)]]
    (if (empty? l)
      o
      (recur (drop 2 l)
             (conj o (apply vector (take 2 l)))))))

(defn eval-list [lst mode]
  (case mode
    1 (reduce #((first %2) %1 (last %2)) (to-pairwise lst))
    2 (let [l (to-pairwise lst)]
        (->> (next l)
             (reduce #(if (= + (eval (first %2)))
                        (update-in %1 [(dec (count %1)) 1] (partial + (last %2)))
                        (conj %1 %2))
                     [[nil (first l)]])
             (#(eval-list (flatten (concat [(last (first %))] (next %))) 1))))))

(defn parse [s]
  (case s
    "+" +
    "*" *
    (Long/parseLong s)))

(defn eval-str [s mode]
  (eval-list (map parse (re-seq #"\d+|[+*]" s)) mode))

(defn eval-line [s mode]
  (eval-str (remove-parens s mode) mode))

(defn day18-1 [in]
  (reduce + (map #(eval-line % 1) in)))

(println (str "Part one: " (day18-1 input)))

(defn day18-2 [in]
  (reduce + (map #(eval-line % 2) in)))

(println (str "Part two: " (day18-2 input)))
