use std::fs::File;
use std::io::{self, BufRead};

fn main() {
    let file = File::open("input").unwrap();
    let sum = io::BufReader::new(file).lines().map(|x| x.unwrap()).map(|line|
        line.split(' ').skip(11).filter(|x| vec![2, 3, 4, 7].contains(&x.len())).count()
    ).sum::<usize>();
    println!("{}", sum);
}
