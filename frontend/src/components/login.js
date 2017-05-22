import React from 'react'
import { Form, Text } from 'react-form'

const LoginForm = (
  <Form
    onSubmit={(values) => {
      console.log('Success!', values)
    }}
    validate={({ name }) => {
      return {
        name: !name ? 'A name is required' : undefined
      }
    }}
  >
    {({submitForm}) => {
      return (
        <form onSubmit={submitForm}>
          <Text field='name' />
          <button type='submit'>Submit</button>
        </form>
      )
    }}
  </Form>
);
const Login = () => (
    <div>
      <div className='table-wrap'>
        <LoginForm
          onSubmit={(values) => {
            window.alert(JSON.stringify(values, null, 2))
          }}
        />
      </div>
    </div>
);
export default Login;