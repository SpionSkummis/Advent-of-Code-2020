(def input (-> "inputs/day04.txt"
               slurp 
               (clojure.string/split #"\n\n")))

(defn valid? [passport]
  (= 7 (count (re-seq #"(?:byr|iyr|eyr|hgt|hcl|ecl|pid)\:" passport))))

(defn day4-1 []
  (count (filter valid? input)))

(defn valid-field? [field]
  (let [check-year (fn [x l u] (and (= 4 (count x))
                                    (<= l (Integer/parseInt x) u)))
        val (nth field 2)]
    (condp = (second field)
      "byr" (check-year val 1920 2002)
      "iyr" (check-year val 2010 2020)
      "eyr" (check-year val 2020 2030)
      "hgt" (let [[_ height unit] (re-find #"(\d+)(cm|in)" val)]
              (condp = unit
                "cm" (<= 150 (Integer/parseInt height) 193)
                "in" (<= 59 (Integer/parseInt height) 76)
                false))
      "hcl" (and (re-find #"#[\d|[a-f]]{6}" val)
                 (= 7 (count val)))
      "ecl" (re-find #"(?:amb|blu|brn|gry|grn|hzl|oth)" val)
      "pid" (and (re-find #"\d{9}" val)
                 (= 9 (count val))))))

(defn valid2? [passport]
  (let [fields (re-seq #"(byr|iyr|eyr|hgt|hcl|ecl|pid):(#{0,1}[\d|a-z]+)" passport)]
    (and (= 7 (count fields))
<<<<<<< HEAD
<<<<<<< HEAD
         (every? valid-field? fields))))

(defn day4-2 []
=======
         (every? #(and (some? %) (not (false? %))) (map valid-field? fields)))))

(defn day4-1 []
>>>>>>> 2749eb554812233338a5fe55b73d80ed03ae2ac9
=======
         (every? #(and (some? %) (not (false? %))) (map valid-field? fields)))))

(defn day4-1 []
>>>>>>> 2749eb554812233338a5fe55b73d80ed03ae2ac9
  (count (filter valid2? input)))
