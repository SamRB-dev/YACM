// Std modules
use std::fs::File;
use std::io;
use std::io::Read;
use std::io::Write;
use std::path::Path;

// pyo3
use pyo3::ffi::c_str;
use pyo3::prelude::*;
use pyo3::types::{IntoPyDict, PyModule};

// chrono
use chrono::prelude::*;

// Function that returns temporary previous entry
pub fn previousEntry(path: &Path) -> Result<String, io::Error> {
    let mut openFile = File::open(path)?;
    let mut dataFromFile: String = String::new();
    openFile.read_to_string(&mut dataFromFile)?;
    Ok(dataFromFile)
}

pub fn writePreviousEntry(path: &Path, contentString: String) -> () {
    let mut contentStorage = File::create(path).expect("Error Occured");
    contentStorage
        .write_all(contentString.as_bytes())
        .expect("Write failed");
}

pub fn writeEntryToPyJson(path: &Path, contentString: String) -> () {
    let time: String = Local::now().format("%d-%m-%Y~%H:%M:%S").to_string();

    Python::with_gil(|py| {
        let code = c_str!(
            "
import json

def write_json(path: str, date: str, content: dict) -> None:
    try:
        with open(path, mode='r') as file:
            file_data = json.load(file)
        file_data[date] = content
        with open(path, mode='w') as update_file:
            json.dump(file_data, update_file, indent=4)
    except Exception as error:
        print(error)
"
        );

        let handler = PyModule::from_code(py, code, c_str!(""), c_str!(""))
            .unwrap()
            .getattr("write_json")
            .unwrap();

        let jsonData = [("content", contentString.as_str())]
            .into_py_dict(py)
            .unwrap();

        handler
            .call1((path.to_str().unwrap(), time.as_str(), jsonData))
            .unwrap();
    });
}
