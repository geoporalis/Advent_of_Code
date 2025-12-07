mod tests;
mod problem;

use std::fs;
//use std::path::Path;

fn read_all_lines(path : String) -> String
{
    let contents : String = fs::read_to_string(path).expect("Should have been able to read the file");
    return contents;
}

fn main()
{
    let file_path : String = String::from("./input");
    //let path = std::path::Path::new("../input");
    println!("{:?}", file_path);
    let file_contents = fs::read_to_string(file_path).expect("Please provide valid file name");
    //let file_contents = read_all_lines(file_path);
 
    let part1 = problem::count_middle_pages_of_updates(&file_contents);
    let part2 = problem::count_middle_pages_of_fixuped_updates(&file_contents);

    println!("Part 1: {}", part1);
    println!("Part 2: {}", part2);
}