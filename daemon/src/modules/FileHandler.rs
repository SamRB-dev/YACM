use std::fs::File;
use std::io::Write;
use std::path::Path;
use std::io::Read;

// crate for handling db file and content checker
pub fn previousEntry(path: &Path) -> String {
    let mut openFile = File::open(path).unwrap();
    let mut dataFromFile: String = String::new();
    openFile.read_to_string(&mut dataFromFile).unwrap();
    return dataFromFile;
}

pub fn writePreviousEntry(path: &Path, contentString: String) -> () {
    let mut contentStorage = File::create(path).expect("Error Occured");
    contentStorage
        .write_all(contentString.as_bytes())
        .expect("Write failed");
}
