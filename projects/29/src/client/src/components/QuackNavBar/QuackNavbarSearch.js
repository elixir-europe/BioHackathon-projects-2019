import React,{useContext, useState} from 'react';
import styled from 'styled-components';
import QuackContext from '../../context';

const Input = styled.input`
    margin-top: 0.7rem;
    margin-left: 1.5rem;
    width: 400px;
    outline: 0;
    border-width: 0 0 0px;
    border-color: black;
    font-family: Dosis;
    font-size: 2rem;
    background-color : #FFFFE0;
    padding-left: 1rem; 

`
const QuackNavbarSearch = () => {
    const {state, dispatch} = useContext(QuackContext);
    const [value, setValue] = useState(state.query);
    const deleteQuery = () => {
        dispatch({type: 'DELETE_SEARCH'})
        setValue('')
    }
    const changeValue = (evt) => {
        setValue(evt.target.value)
        dispatch({type: 'SET_QUERY', data: evt.target.value})

    }
    return (
        <div>
            <Input onChange={(evt)=>changeValue(evt)} onClick={()=>deleteQuery()} value={value} placeholder="type your query"  type="search"/>
        </div>
    );
};

export default QuackNavbarSearch;