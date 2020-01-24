

(defun goal-state (l) 
(cond
	((equal l '(1 2 3 8 e 4 7 6 5)) t)
	(T nil)))


(defun get-direction  (l)
(car l))

(defun gsh (l)
(cond
	((equal l nil) nil)
	(t (append (car l) (gsh (cdr l))))))

(defun get-state (l) 

(gsh (cdr l))
)

(defun same-state ( l m) 
(cond 
	((equal l nil) nil)
	((equal (cdr l)  (cdr m)) t)
	(t nil)))

(defun pathH (l)
(cond 
	((equal l nil) nil)
	(T (append (pathH (cdr l)) (list(caar l)))))
)

(defun path (l)
	(cdr (reverse (mapcar #'get-direction l)))
)


(defun rr-addList (add l) 
(cond
	(add (append l add))
	(t l)))

(defun rr-helper (l 2nd)
(cond
	((not (member l  2nd :test 'same-state))  (list l) )
	(t nil)
))

(defun remove-redundant (l 2nd)
(cond 	
	((equal l nil) nil)
	((equal 2nd nil) l)
	((equal (list-length l) 1) (if (rr-helper l 2nd) l nil))
	(t (rr-addList  (remove-redundant (cdr l) 2nd) (rr-helper (car l) 2nd)))

))

(defun sub (l n)
(substitute 'e 'x (substitute n 'e (substitute 'x n l))))

(defun eL (l)
(position 'e l))

(defun move-u (l  e)
(cond 
	((find (+ e 1) '(4 5 6 7 8 9)) (list 'u (sub l (nth (- e 3) l))))))
	

(defun move-d (l e)
(cond 
	((find  (+ e 1) '(1 2 3 4 5 6 )) (list 'd (sub l  (nth  (+ 3 e) l))))))

(defun move-l (l e)
(cond 
	((find (+ e 1) '( 2 3 5 6 8 9)) (list 'l (sub l (nth (- e 1) l))))
	(t nil)))

(defun move-r (l e)
(cond 
	((find (+ e 1) '(1 2 4 5 7 8)) (list 'r (sub l (nth (+ 1 e) l))))
	(t nil)))

(defun addList (add l) 
(cond
	(add (append l (list add)))
	(t l)))

(defun moves (l)
(addList (move-r l (eL l))
	(addList (move-l l (eL l)) 
		(addList (move-d l (eL l)) 
			(addList (move-u l (eL l)) nil)
		)
		)
	))
	
