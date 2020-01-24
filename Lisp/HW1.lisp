;;; Homework 1 

(defun my-rotate (l) 
(cond
	((equal l nil) nil)
	(T (append (cdr l) (list (car l))))))


(defun my-rotate-n (n l)
(cond 
	((equal n 0) l)
	(T  (my-rotate-n (- n 1) (my-rotate l)))))


(defun first-sat ( x y foo)  (cond((equal x nil) nil)	((equal	y nil) nil)
   		((funcall foo  (car x) (car y)) (list (car x) (car y)))
   		(T (first-sat (cdr x) (cdr y) foo))))

;;;(defun first-sat '(1 4 3 5) '(2 5 1 4) #' (lamnda (x y) ())

(defun my-remove (x l)
(cond 
	((equal l nil) nil)
	((listp (car l)) (append (my-remove x (car l)) (my-remove x (cdr l)) ))
	((equal x (car l))  (my-remove x (cdr l)))
	(T (append (list (car l)) ( my-remove x (cdr l))))))

;;;; Palindorme

(defun palindromep (l)
(cond
	((equal (list-length l) 1) T)
	((equal (list-length l) 0) T)
	((equal (car l) (last l)) (palindromep (cdr (butlast l))))
	(t nil)))


;;; last (until (equal (cdr l) nil) l)