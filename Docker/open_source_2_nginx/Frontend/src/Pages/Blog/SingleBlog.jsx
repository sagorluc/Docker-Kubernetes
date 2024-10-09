import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import axios from "axios";

const SingleBlog = () => {
    const {id} = useParams(); // get the blog id from url
    const [data, setData] = useState([]);

    const singleBlogHandle = async () => {
        try{
            const response = await axios.get(`http://127.0.0.1:8000/blog_list/${id}/`);
            console.log(response.data, 'line 12');
            setData(response.data); // Save the API response in the state
        }catch(error){
            console.error('Error fetching data:', error);
        }
    }

    // Use useEffect to fetch data when the component loads
    useEffect(() => {
        singleBlogHandle(); // Fetch the data when the component mounts
    }, []);


    return (
        <div className="mb-10 max-w-screen-xl mx-auto px-3">
            <div className="pt-10 text-2xl md:text-5xl font-semibold font-serif ">
                <h1>{data.title}</h1>
            </div>
            <div className="py-10 ">
                <img
                    src={`http://127.0.0.1:8000/${data.image}`}
                    alt="Blog image"
                />
            </div>
            <div className="font-serif">
                <p className="mb-2">
                   {data.paragraph} 
                </p>

            </div>
        </div>
    );
};

export default SingleBlog;
