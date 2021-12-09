use std::fs::File;
use std::io::{self, BufRead};
use std::collections::HashMap;

fn get(out: &HashMap::<u32, &str>, target: &str) -> u32 {
    match target {
        x if x.len() == 2 => 1,
        x if x.len() == 3 => 7,
        x if x.len() == 4 => 4,
        x if x.len() == 7 => 8,
        x if x.len() == 5 && out.get(&7).map_or(false, |d| d.chars().all(|c| x.contains(c))) => 3,
        x if x.len() == 6 && out.get(&4).map_or(false, |d| d.chars().all(|c| x.contains(c))) => 9,
        x if x.len() == 6 && out.contains_key(&9) && out.get(&1).map_or(false, |d| d.chars().all(|c| x.contains(c))) => 0,
        x if x.len() == 6 && out.contains_key(&9) && out.contains_key(&0) => 6,
        x if x.len() == 5 && out.contains_key(&6) && out.get(&9).map_or(false, |d| x.chars().all(|c| d.contains(c))) => 5,
        x if x.len() == 5 && out.contains_key(&3) && out.contains_key(&5) => 2,
        _ => 11
    }
}

fn deduce(digits: Vec<&&str>, target: &str) -> u32 {
    let mut out = HashMap::<u32, &str>::new();
    while get(&out, target) == 11 {
        for digit in &digits {
            out.insert(get(&out, digit), digit);
        }
    }
    get(&out, target)
}

fn parse(digits: Vec<&&str>, target: Vec<&&str>) -> u32 {
    target.iter().map(|d| deduce(digits.clone(), d)).fold(0, |a, x| (a*10+x))
}

fn main() {
    let file = File::open("input").unwrap();
    let sum = io::BufReader::new(file).lines().map(|x| x.unwrap()).map(|line| {
        let digits : Vec<&str> = line.split(' ').collect();
        parse(digits.iter().take(10).collect(), digits.iter().skip(11).take(4).collect())
    }).sum::<u32>();
    println!("{}", sum);
}
