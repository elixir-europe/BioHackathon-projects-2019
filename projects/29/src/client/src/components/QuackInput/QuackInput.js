import React, {useContext, useState} from 'react';
import styled from 'styled-components';
import QuackContext from "../../context";
import ReactFilterBox, {SimpleResultProcessing} from "react-filter-box";
import "./QuackInput.css"
import sadDuck from './sad_duck.png';
import happyDuck from './happy_duck.png';
import neutralDuck from './neutral_duck.png';
import testData from '../../testdata/testdata.json';


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

const InputWrapper = styled.span`
    width: 800px;
    display: flex;
    flex-direction: row;
    justify-content:space-around;
`

const QuackFilterBox = styled(ReactFilterBox)`
    width: 600px;
`

const Img = styled.img`
    height: 50px;
     padding-top: 2%;
`

const OPTIONS = [
    {
        columnField: "abstract",
        type: "text"
    },
    {
        columnField: "title",
        type: "text"
    },
    {
        columnField: "year",
        type: "number"
    },
    {
        columnField: "authors",
        type: "text"
    },
    {
        columnField: "topic",
        type: "selection"
    },
    {
        columnField: "doi",
        type: "text"
    }
];
const data = [{topic: 'asdf'},
{topic: 'asdf'},
{topic: 'asdfa'},
{topic: 'gadsg4'},
{topic: 'argag43ga4g'},
{topic: 'g'},
{topic: 'ag'},
{topic: 'a44'},
{topic: 'a4g'},
{topic: 'a4'},
{topic: 'ga4ga4tga'},
{topic: 'rga'},
{topic: 'ta'},
{topic: 'rtaq3'},
{topic: '4ta'},
{topic: 'rga'},
{topic: '4tga'},
{topic: 'ergarag'}]

function QuackInput(props) {
    const {state, dispatch} = useContext(QuackContext);
    const [value, setValue] = useState('')
    const [isOk, setIsOk] = useState(false);


    const handleSubmit = (evt) => {
        if (evt.key === 'Enter') {
            dispatch({type: 'SET_QUERY', data: evt.target.value})
        }

    }
    const onChange = (query, result) => {
        setIsOk(!result.isError)
        setValue(query)
    }
    const renderIcon = () => {
        if (value==''){
            return <Img title="type your query" src={neutralDuck}/>

        }
        return isOk ? <Img title="syntax correct!" src={happyDuck}/> :
            <Img title="syntax error" src={sadDuck}/>
    }

    const onParseOk = (expressions) => {
        console.log(expressions);
        if(value.trim()!=='')
            dispatch({type:'SET_QUERY',value})

            dispatch({type:"SET_RESULTS", data: testData})
    }
    return (

        <InputWrapper>
            <QuackFilterBox
                data={data}
                onChange={(query, result) => onChange(query, result)}
                options={OPTIONS}
                onParseOk={(expr) => onParseOk(expr)}
            />
            {renderIcon()}
        </InputWrapper>

    );
}

export default QuackInput;