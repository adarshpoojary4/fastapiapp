import Welcome from "./components/welcome";
import NavBar from "./components/NavBar";
import CompanyCard from "./components/companycard";
import JobCard from "./components/JobCard";
import Footer from"./components/Footer";
function App(){
  return(
    <>
    <NavBar />
    <Welcome />
    <CompanyCard/>
    <JobCard/>
    <Footer/>
    </>
  )
}

export default App