;;Carlo Gonzaelz Lab


;;-------------------------------------------------------------
;;New work


(defun ofp-helper (_move goal num)
(cond
	((null _move) num)
	((equal (car _move) 'e) (ofp-helper (cdr _move) (cdr goal) num))
	((equal (car _move) (car goal)) (ofp-helper (cdr _move) (cdr goal) num))
	(t (ofp-helper (cdr _move) (cdr goal) (+ 1 num)))))

(defun out-of-place (__move)
	(ofp-helper __move '(1 2 3 8  e 4 7 6 5) 0))



(defun out-of-place-f (_path)
(+ (- (list-length _path) 1) (out-of-place (cadar _path))))


;;, find the row and column of the current tile and where it should be and figure out the differences. 
;; You can use truncate to get the rows and mod to get the columns.

(defun x-distant (target goal)
	(abs (- (floor target 3) (floor goal 3))))

(defun y-distant (target goal)
	(abs (-  (mod target 3) (mod goal 3))))

(defun h-value (target pos)
  (let ((goal (position target '(1 2 3 8 e 4 7 6 5)) ))
  	(+ (x-distant pos goal) (y-distant pos goal))))


(defun manhattan (_state &optional (pos 0))
(cond
 ((equal pos 9 ) 0)
 ((equal (nth pos _state) 'e)  (manhattan  _state (+ pos 1)))
 (t (+  (h-value  (nth pos _state) pos) (manhattan _state (+ 1 pos))))))


(defun manhattan-f (_path)
(+ (- (list-length _path) 1)  (manhattan (cadar _path))))


(defun better (fun)
	#'(lambda (_path1 _path2) (<= (funcall fun _path1) (funcall fun _path2))))


(defun search-a* (olist h)
	(cond
		((null olist) nil)
		((goal-state (get-state (caar olist))) (path (car olist)))
		(t (search-a* (sort (append (cdr olist) (extend-path (car olist))) (better h)  ) h)	)))


;;(defun SSS (state (&key (type 'BFS) (depth 7)  (f #'out-of-place-f )))
 (defun SSS (state  &optional &key (type 'BFS) (depth 7)  (f #'out-of-place-f ))
   (cond
   ((goal-state state) nil)
   ((equal type 'BFS) (search-BFS (make-open-init state)))
   ((equal type 'DFS) (search-DFS (make-open-init state) depth))
   ((equal type 'ID) (search-ID (make-open-init state)))
   ((equal type 'A*) (search-a* (make-open-init state) f))
   ))



	