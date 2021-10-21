;; Auto-generated. Do not edit!


(when (boundp 'basics::WordCount)
  (if (not (find-package "BASICS"))
    (make-package "BASICS"))
  (shadow 'WordCount (find-package "BASICS")))
(unless (find-package "BASICS::WORDCOUNT")
  (make-package "BASICS::WORDCOUNT"))
(unless (find-package "BASICS::WORDCOUNTREQUEST")
  (make-package "BASICS::WORDCOUNTREQUEST"))
(unless (find-package "BASICS::WORDCOUNTRESPONSE")
  (make-package "BASICS::WORDCOUNTRESPONSE"))

(in-package "ROS")





(defclass basics::WordCountRequest
  :super ros::object
  :slots (_words ))

(defmethod basics::WordCountRequest
  (:init
   (&key
    ((:words __words) "")
    )
   (send-super :init)
   (setq _words (string __words))
   self)
  (:words
   (&optional __words)
   (if __words (setq _words __words)) _words)
  (:serialization-length
   ()
   (+
    ;; string _words
    4 (length _words)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _words
       (write-long (length _words) s) (princ _words s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _words
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _words (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass basics::WordCountResponse
  :super ros::object
  :slots (_count ))

(defmethod basics::WordCountResponse
  (:init
   (&key
    ((:count __count) 0)
    )
   (send-super :init)
   (setq _count (round __count))
   self)
  (:count
   (&optional __count)
   (if __count (setq _count __count)) _count)
  (:serialization-length
   ()
   (+
    ;; uint32 _count
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; uint32 _count
       (write-long _count s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; uint32 _count
     (setq _count (sys::peek buf ptr- :integer)) (incf ptr- 4)
   ;;
   self)
  )

(defclass basics::WordCount
  :super ros::object
  :slots ())

(setf (get basics::WordCount :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get basics::WordCount :datatype-) "basics/WordCount")
(setf (get basics::WordCount :request) basics::WordCountRequest)
(setf (get basics::WordCount :response) basics::WordCountResponse)

(defmethod basics::WordCountRequest
  (:response () (instance basics::WordCountResponse :init)))

(setf (get basics::WordCountRequest :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get basics::WordCountRequest :datatype-) "basics/WordCountRequest")
(setf (get basics::WordCountRequest :definition-)
      "string words
---
uint32 count
#uint32 len_count

")

(setf (get basics::WordCountResponse :md5sum-) "58903d21a3264f3408d79ba79e9f7c7e")
(setf (get basics::WordCountResponse :datatype-) "basics/WordCountResponse")
(setf (get basics::WordCountResponse :definition-)
      "string words
---
uint32 count
#uint32 len_count

")



(provide :basics/WordCount "58903d21a3264f3408d79ba79e9f7c7e")


