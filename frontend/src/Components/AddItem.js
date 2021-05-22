import React from "react";
import axios from "axios";
//import ImageUploader from "react-images-upload";
import { withStyles } from '@material-ui/core/styles';
import TextField from '@material-ui/core/TextField';
import MenuItem from '@material-ui/core/MenuItem';
import Button from '@material-ui/core/Button';
import FormData from 'form-data'
import FormControl from '@material-ui/core/FormControl';

const useStyles = theme => ({
  fab: {
    position: 'fixed',
    bottom: theme.spacing(2),
    right: theme.spacing(2),
  },
  input: {
    display: 'none',
  },
    });
  
    const categories = [
      {
        value: 1,
        label: 'Lunch',
      },
      {
        value: 2,
        label: 'Dinner',
      }
    ];


    const specialMealOptions = [
      {
        value: true,
        label: 'YES',
      },
      {
        value: false,
        label: 'NO',
      }
    ];
class AddItem extends React.Component {
  state = {
    meal_name: "",
    price: 0,
    photo:'',
    //image: null,
    categories:[],
    quantity: 0,
    selectedCategory:'',
    data : { 
     meal_name:"",
     price:'', 
     special_meal:false,
     specialMealLabel:'',
     quantity:0,
     category:'',
     photo_main:''
    }

    }
    
  

  
  handleChange = (event) => {
    const target = event.target;
    const value = target.value;
    const name = target.name;
  
   this.setState({

    [name]: value,
   })

   
    };





  showFile = () => {
    if (window.File && window.FileReader && window.FileList && window.Blob) {
       //  var preview = document.getElementById('show-text');
         var file = document.querySelector('input[type=file]').files[0];
         var fileName = document.querySelector('input[type=file]').files[0].name;
     
        console.log(file)
         const validImageTypes = ["image/gif",  "image/jpeg", "image/png"];

         if (!validImageTypes.includes(file.type)) {
          console.log('file is not  valid image')
         } else {
         
            let data = new FormData();
            data.append('file', file, fileName); 
            this.setState({photo_main:file})
            console.log('file')
            console.log(file)
            }
   } else {
      alert("Your browser is too old to support HTML5 File API");
   }
  }

  handleSubmit = (event) => {
    event.preventDefault();
  var  data = {
      meal_name: this.state.meal_name,
      quantity: this.state.quantity,
      category:this.state.category,
      photo_main: this.state.photo_main,
      special_meal: this.state.special_meal
    }
    console.log('Data:')
    console.log(data)
    this.postItem(data);



  };

  postItem = (data)=> {
    axios.post('http://localhost:8000/items/', data, {
      headers: {
        'accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': `multipart/form-data; boundary=${data._boundary}`,
      }
    })
      .then((response) => {
       console.log(response)
      }).catch((error) => {
      console.log(error)
      });
}

getCategories = () =>{
  axios.get(`http://localhost:8000/categories/`)
  .then(res => {
      console.log('categories:')
      console.log(res.data)
var categ=[]
 var cat = res.data.map((category) =>{
        const v = {value: category.id, label: category.name};
        categ.push(v)

      });
      console.log('countries from api:')
      console.log(cat)
      return cat

  })
    .catch((error) => {
    console.log(error)
    return []
    });

}

componentDidMount() {
    var categoriesfromApi = this.getCategories()
    console.log('cat from api:')
    console.log(categoriesfromApi)
    this.setState({categories: categoriesfromApi});

}
  
  render() {

    const { classes } = this.props;
    return (
      <div style={{ padding: 15 }}>
      <form className={classes.root} autoComplete="off">
      <TextField id="outlined-basic" onChange={this.handleChange} name="meal_name" label="Meal Name" variant="outlined" />
      <TextField id="outlined-basic" onChange={this.handleChange} name="price"label="Price" variant="outlined" />
      <TextField id="outlined-basic" onChange={this.handleChange} name="quantity"label="Quantity" variant="outlined" />
  
      <TextField id="outlined-basic" name="special" label="Special " variant="outlined" />
      <div style={{ margin: 10 }}>
      <FormControl fullWidth className={classes.margin} variant="outlined">
      <TextField
          id="standard-select"
          select
          label="Select a category"
          name="category"
          value={this.state.category}
          onChange={this.handleChange}
          helperText="Please select a category"
        >
          { categories.map((option) => (
            <MenuItem key={option.value} value={option.value}>
              {option.label}
            </MenuItem>
          ))
        }

        </TextField>
        </FormControl>
        </div>
        <div style={{ margin: 10 }}>
        <FormControl fullWidth className={classes.margin} variant="outlined">
        <TextField
        id="standard-select"
        select
        label="Is this a special meal"
        name="special_meal"
        value={this.state.special_meal}
        onChange={this.handleChange}
        helperText="Is this a special meal"
      >
        { specialMealOptions.map((option) => (
          <MenuItem key={option.value} value={option.value}>
            {option.label}
          </MenuItem>
        ))
      }
      </TextField>
      </FormControl>
      </div>
      <div style={{ margin: 10 }}>
        <input type="file" 
        accept="image/*" 
        multiple
        onChange={this.showFile}  /> 
        </div>
        <div style={{ margin: 10 }}>
        <Button variant="contained" color="primary"   onClick={this.handleSubmit}>
        Submit
      </Button>
      </div>
    </form>
    </div>
    );
  }
}
export default withStyles(useStyles)(AddItem);