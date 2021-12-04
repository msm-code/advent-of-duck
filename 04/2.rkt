#lang racket

(define (transpose xss) (apply map list xss))
(define (score xss) (apply + (flatten xss)))
(define (zeroes? xss) (andmap zero? xss))
(define (wins? xss) (or (ormap zeroes? xss) (ormap zeroes? (transpose xss))))
(define (replace xss x with) (map (lambda (e) (if (= x e) with e)) xss)) 
(define (replace2d xss x with) (map (lambda (e) (replace e x with)) xss))

(define (tobingo list) (map (lambda (l) (map string->number (string-split l))) list))
(define (bingos list) (if (empty? list)
    '()
    (cons (tobingo (take (cdr list) 5)) (bingos (drop list 6)))))
(define (play bingo nums round last) (if (wins? bingo)
    (cons round (* last (score bingo)))
    (play (replace2d bingo (car nums) 0) (cdr nums) (+ 1 round) (car nums))))

(let* (
    [test (file->lines "input")]
    [numbers (map string->number (string-split (car test) ","))]
    [lines (cdr test)]
    [play1 (lambda (b) (play b numbers 0 0))])
    (println (cdar (sort (map play1 (bingos lines)) > #:key car))))
