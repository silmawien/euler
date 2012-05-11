(defun english-length (s)
    (length
      (remove-if
        (lambda (c) (find c '(#\Space #\-)))
        (format nil "~r" s))))

(print (loop for i from 1 upto 1000 sum (english-length i)))
