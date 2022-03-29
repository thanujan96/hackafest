// {% load static %}
function viewCSVFile(theFile) {
    var fileSize = 0;
    //get file
    // var  = document.getElementById("fileToUpload");

    var regex = /^([a-zA-Z0-9\s_\\.\-:])+(.csv|.txt)$/;
    //check if file is CSV
    if (regex.test(theFile.value.toLowerCase())) {
        //check if browser support FileReader
        if (typeof(FileReader) != "undefined") {
            //get table element
            var table = document.getElementById("myTable");
            var headerLine = "";
            //create html5 file reader object
            var myReader = new FileReader();
            // call filereader. onload function
            myReader.onload = function(e) {
                    var content = myReader.result;
                    //split csv file using "\n" for new line ( each row)
                    var lines = content.split("\r");
                    //loop all rows
                    for (var count = 0; count < lines.length; count++) {
                        //create a tr element
                        var row = document.createElement("tr");
                        //split each row content
                        var rowContent = lines[count].split(",");
                        //loop throw all columns of a row
                        for (var i = 0; i < rowContent.length; i++) {
                            //create td element 
                            var cellElement = document.createElement("td");
                            if (count == 0) {
                                cellElement = document.createElement("th");
                            } else {
                                cellElement = document.createElement("td");
                            }
                            //add a row element as a node for table
                            var cellContent = document.createTextNode(rowContent[i]);

                            cellElement.appendChild(cellContent);
                            //append row child
                            row.appendChild(cellElement);
                        }
                        //append table contents
                        myTable.appendChild(row);
                    }
                }
                //call file reader onload
            myReader.readAsText(theFile.files[0]);
        } else {
            alert("This browser does not support HTML5.");
        }

    } else {
        alert("Please upload a valid CSV file.");
    }
    return false;
}

const dropArea = document.querySelector('.drag-area');
const dragText = document.querySelector('.header');

let button = dropArea.querySelector('.browsebutton');
let input = dropArea.querySelector('input');

let file;
// when file is inside drag area
dropArea.addEventListener('dragover', (event) => {
    event.preventDefault();
    dropArea.classList.add('active');
    dragText.textContent = 'Release to Upload';
    // console.log('File is inside the drag area');
});

function displayFile() {
    let fileType = file.type;
    // console.log(fileType);

    let validExtensions = ['application/vnd.ms-excel'];

    if (validExtensions.includes(fileType)) {
        // console.log('This is an image file');
        let fileReader = new FileReader();

        fileReader.onload = () => {
            let fileURL = fileReader.result;
            // console.log(fileURL);
            var thisFile = document.getElementById("fileToUpload");
            viewCSVFile(thisFile)
            document.getElementById("btnUploadFile").style.display = "inline";
            document.getElementById("viewfilebutton").style.display = "inline";
            let imgTag = `<img  width="182px" src="static/images/my/csv.png" alt="">`;
            dropArea.innerHTML = imgTag;
        };
        fileReader.readAsDataURL(file);
    } else {
        alert('This is not an CSV File');
        dropArea.classList.remove('active');
    }
}
button.onclick = () => {
    input.click();
};

// when browse
input.addEventListener('change', function() {
    file = this.files[0];
    dropArea.classList.add('active');
    displayFile();
});


function viewFile() {
    if (document.getElementById('myTable').style.display == "none") {
        document.getElementById("myTable").style.display = "block";
        document.getElementById("viewfilebutton").innerHTML = "Hide preview";

    } else {
        document.getElementById("myTable").style.display = "none";
        document.getElementById("viewfilebutton").innerHTML = "View File";

    }
}

function collectionEdit(collectionId) {
    console.log(collectionId)
    if (document.getElementById("colleditbutton" + collectionId).innerHTML == "Edit") {
        document.getElementById("colleditbutton" + collectionId).innerHTML = "Cancel"
        document.getElementById("editcollection" + collectionId).style.display = 'inline-grid';
        document.getElementById("collname" + collectionId).style.display = 'none';
        document.getElementById("colldelete" + collectionId).style.display = 'block';
    } else {
        document.getElementById("colleditbutton" + collectionId).innerHTML = "Edit"
        document.getElementById("editcollection" + collectionId).style.display = 'none';
        document.getElementById("collname" + collectionId).style.display = 'block';
        document.getElementById("colldelete" + collectionId).style.display = 'none';
    }

}

function collectionAdd(collectionId) {
    const buttonText = document.getElementById("colleditbutton" + collectionId).innerHTML;
    if (buttonText == "New Experiment") {
        document.getElementById("colleditbutton" + collectionId).innerHTML = "Cancel"
        document.getElementById("editcollection" + collectionId).style.display = 'inline-grid';
        document.getElementById("collname" + collectionId).style.display = 'none';
    } else {
        document.getElementById("colleditbutton" + collectionId).innerHTML = "New Experiment"
        document.getElementById("editcollection" + collectionId).style.display = 'none';
        document.getElementById("collname" + collectionId).style.display = 'block';
    }

}