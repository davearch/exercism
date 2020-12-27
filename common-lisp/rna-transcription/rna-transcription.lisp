(in-package #:cl-user)
(defpackage #:rna-transcription
  (:use #:cl)
  (:export #:to-rna)
  (:export #:*DNA-to-RNA*))
(in-package #:rna-transcription)

(defparameter *DNA-to-RNA* (pairlis '(#\G #\C #\T #\A) '(#\C #\G #\A #\U)))

(defun to-rna (str)
  "Transcribe a string representing DNA nucleotides to RNA."
  (with-output-to-string (*standard-output*)
    (loop for dna-char across str
          for rna-char = (cdr (assoc dna-char *DNA-to-RNA*))
          do (if rna-char
                 (princ rna-char)
                 (error "invalid dna string")))))
