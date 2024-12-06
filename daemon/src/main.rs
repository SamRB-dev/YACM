// External crates
extern crate copypasta;

// Declare modules
mod modules;

// Use modules
use copypasta::{ClipboardContext, ClipboardProvider};
use modules::FileHandler;
use std::path::Path;

fn main(){
    let mut ctx = ClipboardContext::new().unwrap();
    let mut content: String = String::new();
    // let mut contentNewline: String = String::new();
    let previous_entry_path: &Path = Path::new("../db/previousEntry.txt");
    loop {
        content = ctx.get_contents().unwrap();
        // contentNewline = content.clone() + "\n";
        if content != FileHandler::previousEntry(previous_entry_path).unwrap() {
            FileHandler::writePreviousEntry(previous_entry_path, content.clone());
            FileHandler::writeEntryToPyJson(Path::new("../db/db.json"),content);
        }
    }
}
