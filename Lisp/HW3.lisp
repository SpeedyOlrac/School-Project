

(defun goal-state (l) 
(equal l '(1 2 3 8 e 4 7 6 5)))


(defun get-direction  (l)
(car l))

(defun get-state (l) 
(first (rest l)))

(defun same-state (move1 move2)
 (equal (get-state move1) (get-state move2)))

(defun path (pathlist)
 (rest (reverse (mapcar 'get-direction pathlist))))


;;(defun remove-redundant (l 2nd)
;;(cond 	
;;	((equal l nil) nil)
;;	((equal 2nd nil) l)
;;	((equal (list-length l) 1) (if (rr-helper l 2nd) l nil))
;;	(t (rr-addList  (remove-redundant (cdr l) 2nd) (rr-helper (car l) 2nd)))))

(defun remove-redundant (list1 list2)
 (cond 
   ((null list1) nil)
   ((member (first list1) list2 :test #'same-state)
      (remove-redundant (rest list1) list2))
   (t (cons (first list1) (remove-redundant (rest list1) list2)))))


; Gets position of e in a board configuration
(defun getepos (state)
  (position 'e state))

; Swaps e and whatever value is at position n in state
(defun swap-e-with-n (state n)
  (let ((val (nth n state)))
    (substitute 'e 'x (substitute val 'e (substitute 'x val state)))))

; If moving down is legal from state, this function returns the resulting
; move in a list.  If moving down is not legal, an empty list is returned.
(defun move-down (state)
  (let ((epos (getepos state)))
       (if (> epos 5) () (list (list 'D (swap-e-with-n state (+ epos 3)))))))

; If moving up is legal from state, this function returns the resulting
; move in a list.  If moving up is not legal, an empty list is returned.
(defun move-up (state)
  (let ((epos (getepos state)))
       (if (< epos 3) () (list (list 'U (swap-e-with-n state (- epos 3)))))))

; If moving left is legal from state, this function returns the resulting
; move in a list.  If moving left is not legal, an empty list is returned.
(defun move-left (state)
  (let ((epos (getepos state)))
       (if (eq (mod epos 3) 0) 
           () 
           (list (list 'L (swap-e-with-n state (- epos 1)))))))

; If moving right is legal from state, this function returns the resulting
; move in a list.  If moving right is not legal, an empty list is returned.
(defun move-right (state)
  (let ((epos (getepos state)))
       (if (eq (mod epos 3) 2) 
           () 
           (list (list 'R (swap-e-with-n state (+ epos 1)))))))

 
; This is the main function (the only one that you need to call
; from your code).  It returns a list of the legal moves from the
; given state 
(defun moves (state)
  (append (move-down state)
          (move-up state)
          (move-left state)
          (move-right state)))
	
;; Lab 3

(defun make-open-init (inital) 
	( list (list (list '() inital))))



(defun expath_helper (moves _path)
(if
   (ENDP moves) nil
   (cons (cons  (first moves)  _path) (expath_helper (cdr moves) _path))))

;;In expath-helper, you want to cons a move onto the path to create a new path.
;; You then want to cons this new path onto the list of paths that you're recursively forming

(defun extend-path (_path) ;; ( path) (init path)
 (expath_helper (remove-redundant (moves (get-state (first _path))) _path)  _path))

;;cadaar


;; call path when path is found

;;(defun bfs-helper (_list)
;;(cond
;;	((equal _list nil) nil)
;;	((goal-state (cdar _list)) ())

;;mantain a openlist check each one before doing down.
;;	))


(defun search-bfs (state) ;; states are paths
(cond
	((equal state nil) nil)
	((goal-state (cadaar state))  (path (cdar state)))
	(t  (search-bfs (append (cdr state) (extend-path (car state))) ))

	))
	;; (u d l r ) breath first
 
 ;; '(((U (2 8 3 1 e 4 7 6 5)) (NIL (2 8 3 1 6 4 7 e 5)))((L (2 8 3 1 6 4 e 7 5)) (NIL (2 8 3 1 6 4 7 e 5)))((R (2 8 3 1 6 4 7 5 e)) (NIL (2 8 3 1 6 4 7 e 5)))))


 ;;(dropFirst (make-open-init '((1 2 3 e 8 4 7 6 5)))))

(defun search-dfs-fd (state depth)
(cond
	;;((equal (print  (cadaar state)) nil) nil)
	;;((goal-state (cadaar state)) (path state))
	;;((goal-state (cadaar state))   (path (car state)))
	;;((> depth 1 ) (search-dfs-fd (cons (extend-path ( car state)) (cdr state)) (- depth 1)))
	;;(t (search-dfs-fd (cons (extend-path ( cadr state)) (cddr state)) 3))
		;; pick the first one, goes depth down the goes back to nieghboring stuff

	));; (u d l r)

(defun id_helper (state &optinal depth)
;;(cons  
	;;((equal state nil) nil)
	;;((goal-state state) (path state))
	;;(( (id_helper(car (extend-path state)) depth))  )
;;	)
)


(defun search-id (state &optional depth)
(cons
	;;((null state) nil)
	;;((goal-state state) (path state))
	;;(())

	;;(t (search-id (append (cdr state) (extend-path ( car state))) (+ 1 depth)))
	;; bfs
	))

	;;go down on path till depth is hit then try next path

	;;( u d l r) iterative deepening


(defun sss (inital ? ?)
	

	)