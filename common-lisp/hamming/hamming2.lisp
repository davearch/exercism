(defpackage #:hamming
  (:use #:cl)
  (:export #:distance))
(in-package #:hamming)

(defun distance (string1 string2)
  "Number of positional differences in two strings of equal length."
  (labels ((sub-distance (string1 string2 counter)
	     ;; when the length is zero return zero
	     (cond ((or (zerop (length string1)) (zerop (length string2)))
		    counter)
		   ;; when lengths are the same, get sub-distance
		   ;; otherwise (implicitly) return nil
		   ((= (length string1) (length string2))
		    (sub-distance (subseq string1 1)(subseq string2 1)
				  (if (not (string= (subseq string1 0 1) (subseq string2 0 1)))
				      (incf counter)
				      counter))))))
    (sub-distance string1 string2 0)))
