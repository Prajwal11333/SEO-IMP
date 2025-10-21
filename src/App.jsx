



// import { useState, useEffect } from "react";
// import Sidebar from "./components/Sidebar";
// import Dashboard from "./components/Dashboard";
// import SEOAnalyzer from "./components/SEOAnalyzer";
// // // import PredictPerformance from './components/PredictPerformance'
// // // import CompetitorInsights from './components/CompetitorInsights'
// import { Toaster } from "react-hot-toast";
// import HomeLanding from "./components/HomeLanding";

// function App() {
//   const [activeTab, setActiveTab] = useState("home");
//   const [darkMode, setDarkMode] = useState(false);

//   useEffect(() => {
//     if (darkMode) {
//       document.documentElement.classList.add("dark");
//     } else {
//       document.documentElement.classList.remove("dark");
//     }
//   }, [darkMode]);

//   const renderContent = () => {
//     switch (activeTab) {
//       case "home":
//         return <HomeLanding setActiveTab={setActiveTab} />;
//       case "dashboard":
//         return <Dashboard />;
//       case "analyzer":
//         return <SEOAnalyzer />;
//       default:
//         return <HomeLanding setActiveTab={setActiveTab} />;
//     }
//   };

//   return (
//     <div
//       className={`min-h-screen ${
//         darkMode ? "dark bg-gray-950" : "bg-gray-50"
//       } transition-colors duration-300`}
//     >
//       <Sidebar
//         activeTab={activeTab}
//         setActiveTab={setActiveTab}
//         darkMode={darkMode}
//         setDarkMode={setDarkMode}
//       />

//       <div className="ml-64 p-0 overflow-hidden">
//         {renderContent()}
//       </div>

//       <Toaster position="top-right" />
//     </div>
//   );
// }

// export default App;



import { useState, useEffect } from "react";
import Dashboard from "./components/Dashboard";
import SEOAnalyzer from "./components/SEOAnalyzer";
import { Toaster } from "react-hot-toast";
import HomeLanding from "./components/HomeLanding";

function App() {
  const [activeTab, setActiveTab] = useState("home");
  const [darkMode, setDarkMode] = useState(true); // Default to dark mode

  useEffect(() => {
    if (darkMode) {
      document.documentElement.classList.add("dark");
    } else {
      document.documentElement.classList.remove("dark");
    }
  }, [darkMode]);

  const renderContent = () => {
    switch (activeTab) {
      case "home":
        return <HomeLanding setActiveTab={setActiveTab} />;
      case "dashboard":
        return <Dashboard />;
      case "analyzer":
        return <SEOAnalyzer />;
      default:
        return <HomeLanding setActiveTab={setActiveTab} />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-950 transition-colors duration-300">
      {/* Main Content - No Sidebar */}
      <div className="w-full">
        {renderContent()}
      </div>

      <Toaster position="top-right" />
    </div>
  );
}

export default App;