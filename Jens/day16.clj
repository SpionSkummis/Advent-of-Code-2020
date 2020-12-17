(def input (let [in (slurp "inputs/day16.txt")]
             {:my-ticket (re-find #"(?<=your ticket:\n)(?:\d+,)+\d+" in)
              :nearby-tickets (re-seq #"(?<!your ticket:)(?<=\n)(?:\d+,)+\d+" in)
              :fields (re-seq #"[a-z ]+: \d+-\d+ or \d+-\d+" in)}))

(def fields (->> (:fields input)
                 (mapcat #(re-seq #"([a-z ]+)\: (\d+)-(\d+) or (\d+)-(\d+)" %))
                 (map next)
                 (map (fn [x] (into [(first x)] (map #(Integer/parseInt %) (next x)))))))

(def all-valid (set (mapcat #(concat (range (nth % 1) (nth % 2))
                                     (range (nth % 3) (nth % 4))) fields)))

(def nearby-tickets (->> (:nearby-tickets input)
                         (map #(re-seq #"\d+" %))
                         (map (fn [x] (map #(Integer/parseInt %) x)))))

(defn day16-1 []
  (reduce + (mapcat (partial remove #(contains? all-valid %)) nearby-tickets)))

(def my-ticket (map #(Integer/parseInt %) (re-seq #"\d+" (:my-ticket input))))

(defn valid? [x]
  (every? #(contains? all-valid %) x))

(defn possible-class? [vals class]
  (every? #(or (<= (nth class 1) % (nth class 2))
               (<= (nth class 3) % (nth class 4))) vals))

(defn extract-departure-fields []
  (let [ticket-cols (apply map vector (filter valid? nearby-tickets))]
    (loop [possible-fields (map (fn [x] (map #(possible-class? % x) ticket-cols)) fields)
           found-fields    []]
      (if (= 20 (count found-fields))
        (map second (filter #(re-find #"departure" (first %)) found-fields))
        (let [[field-id _] (some #(when (= 1 (last %)) %)
                                 (map-indexed #(vector %1 (count (filter true? %2)))
                                              possible-fields))
              col          (reduce #(if (= true %2) (reduced %1) (inc %1)) 0
                                   (nth possible-fields field-id))]
          (recur (map (fn [x] (reduce #(if (= (count %1) col)
                                         (conj %1 false)
                                         (conj %1 %2)) [] x)) possible-fields)
                 (conj found-fields [(first (nth fields field-id)) col])))))))

(defn day16-2 []
  (reduce * (map #(nth my-ticket %) (extract-departure-fields))))
