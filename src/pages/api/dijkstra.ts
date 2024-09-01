// pages/api/dijkstra.ts

import type { NextApiRequest, NextApiResponse } from 'next';
import { spawn } from 'child_process';
import path from 'path';

type DijkstraResult = {
  distances: { [key: string]: number };
  path: { [key: string]: string | null };
};

export default function handler(req: NextApiRequest, res: NextApiResponse) {
  // Only allow POST requests
  if (req.method === 'POST') {
    const { graph, start } = req.body;

    // Define the path to the Python script
    const pythonScript = path.join(process.cwd(), 'python-scripts', 'dijkstra.py');

    // Spawn a child process to run the Python script
    const pyProcess = spawn('python3', [pythonScript]);

    // Write data to the Python script
    pyProcess.stdin.write(JSON.stringify({ graph, start }));
    pyProcess.stdin.end();

    // Initialize a variable to store the output from the Python script
    let result = '';

    // Listen for data from the Python script
    pyProcess.stdout.on('data', (data) => {
      result += data.toString();
    });

    // Handle errors from the Python script
    pyProcess.stderr.on('data', (data) => {
      console.error('Error from Python script:', data.toString());
    });

    // Handle the close event, which indicates the Python script has finished executing
    pyProcess.on('close', (code) => {
      if (code !== 0) {
        return res.status(500).json({ error: 'Failed to run Python script' });
      }
      try {
        const parsedResult: DijkstraResult = JSON.parse(result);
        res.status(200).json(parsedResult);
      } catch (error) {
        res.status(500).json({ error: 'Failed to parse Python script output' });
      }
    });
  } else {
    // If the request method is not POST, return a 405 Method Not Allowed
    res.setHeader('Allow', ['POST']);
    res.status(405).end(`Method ${req.method} Not Allowed`);
  }
}
