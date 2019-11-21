import React,{useReducer} from 'react';
import QuackSearch from './pages/QuackSearch';
import QuackResults from './pages/QuackResults';
import QuackContext from "./context";
import reducer from "./reducer";
import './App.css';

const initialState = {
    query: '',
    expressions: [],
    results: [],
    happyCount: 0
}

function App() {
        const [state, dispatch] = useReducer(reducer, initialState)

  return (

        <QuackContext.Provider value={{state, dispatch}}>
            {state.results.length>0?<QuackResults/>:<QuackSearch/>}
        </QuackContext.Provider>
  );
}

export default App;

