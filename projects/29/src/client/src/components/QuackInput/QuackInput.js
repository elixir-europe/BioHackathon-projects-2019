import React, {useContext, useState} from 'react';
import styled from 'styled-components';
import QuackContext from "../../context";

const Input = styled.input`
    margin-top: 3rem;
    padding-left: 0.5rem;
    width: 800px;
    font-size:3rem;
    outline: 0;
    border-width: 0 0 4px;
    border-color: black;
    font-family: Dosis;
`

function QuackInput(props) {
    const {state, dispatch} = useContext(QuackContext);
    const [value, setValue] = useState('')
    const setQuery = (evt) => {
        setValue(evt.target.value)
        console.log("pressed", evt)
    }

    const handleSubmit = (evt) =>{
        if (evt.key === 'Enter') {
            dispatch({type: 'SET_QUERY', data: evt.target.value})
        }

    }
    return (
        <div>
            <Input onKeyDown={(evt)=>handleSubmit(evt)} onChange={(evt) => setQuery(evt)} value={value} placeholder="type your query" type="search"/>
        </div>
    );
}

export default QuackInput;