use std::fs;

fn main() {
    let file_path = "./advent5.txt";
    let file_text = fs::read_to_string(file_path).unwrap();
    let commands: Vec<Vec<usize>> = file_text
        .split("\r\n")
        .map(|x| x.to_string())
        .map(|x| x.replace("move ",""))
        .map(|x| x.replace(" from ", " "))
        .map(|x| x.replace(" to ", " "))
        .map(|x| x
            .split(" ")
            .map(|y| y.parse::<usize>().unwrap())
            .collect::<Vec<usize>>())
        .collect();
    let mut bays: [Vec<char>; 9] = ["SCVN","ZMJHNS","MCTGJND","TDFJWRM","PFH","CTZHJ","DPRQFSLZ","CSLHDFPW","DSMPFNGZ"]
        .into_iter()
        .map(|x| x.chars().collect::<Vec<char>>())
        .collect::<Vec<Vec<char>>>()
        .try_into()
        .unwrap();
    for command in commands.into_iter(){
        let from_stack = bays[command[1]-1].clone();
        let to_stack = bays[command[2]-1].clone();
        let moved_crates = from_stack.len()-command[0];
        bays[command[2]-1] = [to_stack, from_stack[moved_crates..].to_vec().into_iter().rev().collect()].concat();
        bays[command[1]-1] = bays[command[1]-1][..moved_crates].to_vec();
    }
    println!("{bays:?}");
}
