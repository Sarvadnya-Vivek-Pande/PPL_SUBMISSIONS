(print "How many numbers u want to enter in a list : ")
(setq m (read))

(setq a nil)
(setq j 0)


(loop
 (setq j (+ j 1))
 (print "Enter a number : ")
 (push (read) a)
 (when (= j m)(return))
)


(print "Enter position of a number u want to find  : ")
(setq n (read))

(setq j m)

(loop
 (if (= n 0) (return (print "Not Found")))
 (if (= j n) (return (print (pop a)))  (pop a))
 (if (= j 0) (return (print "Not Found")))
 (setq j (- j 1))
)

