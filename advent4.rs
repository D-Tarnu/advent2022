extern crate regex;
use regex::Regex;
use std::fs;

fn overlap(x : Vec<&str>) -> u16 {
    let x: Vec<u16> = x.into_iter().map(|y| y.parse::<u16>().unwrap()).collect();
    if x[0] <= x[2] && x[1] >= x[3]{
        return 1;
    }
    else if x[0] >= x[2] && x[1] <= x[3] {
        return 1;
    }
    else {
        return 0;
    }
}
fn main() {
    let file_path: &str = "./advent.txt";
    let schedules= fs::read_to_string(file_path).expect("Should have been able to read the file");
    let schedules: Vec<&str> = schedules.split("\r\n").collect();
    let re = Regex::new(r"\D+").expect("Invaled regex");
    let schedules: Vec<Vec<&str>> = schedules
        .into_iter()
        .map(|x| re
            .split(x)
            .collect::<Vec<&str>>()
        )
        .collect();
    let schedules: Vec<u16> = schedules
        .into_iter()
        .map(|x| overlap(x))
        .collect();
    let answer: u16 = schedules.into_iter().sum();

    println!("{answer:#?}");
}