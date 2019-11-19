import React,{useReducer} from 'react';
import QuackSearch from './pages/QuackSearch';
import QuackResults from './pages/QuackResults';
import QuackContext from "./context";
import reducer from "./reducer";
import './App.css';
import results from './testdata/testdata.json';

const initialState = {
    query: 'gene signatures',
    results: results
}

function App() {
        const [state, dispatch] = useReducer(reducer, initialState)

  return (

        <QuackContext.Provider value={{state, dispatch}}>
            {state.results ?
            <QuackResults/>:<QuackSearch/>}
        </QuackContext.Provider>
  );
}

export default App;

