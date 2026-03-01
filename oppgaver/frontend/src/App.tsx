import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import "./styles/App.css";
import { GeneratorPage } from "./pages/GeneratorPage";
import { CoverImageListPage } from "./pages/CoverImageListPage";
import { Navbar } from "./components/Navbar/Navbar";
import { PlaylistsPage } from "./pages/PlaylistsPage";

function App() {
  return (
    <div>
      <Router>
        <div className="header-container">
          <Navbar />
        </div>

        <div className="content">
          <Routes>
            {/* TODO 1.1: Add route for PlaylistPage*/}
            <Route path="/" element={<PlaylistsPage />} />
            <Route path="/cover/:playlistId" element={<GeneratorPage />} />
            <Route path="/gallery" element={<CoverImageListPage />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
}

export default App;
