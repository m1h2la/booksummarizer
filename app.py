import { useState } from 'react';
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Tabs, TabsList, TabsTrigger, TabsContent } from "@/components/ui/tabs";
import { Textarea } from "@/components/ui/textarea";

export default function Dashboard() {
  const [file, setFile] = useState(null);
  const [summary, setSummary] = useState('');
  const [topicSummary, setTopicSummary] = useState('');
  const [bookConcept, setBookConcept] = useState('');

  const handleFileUpload = (e) => {
    if (e.target.files && e.target.files.length > 0) {
      setFile(e.target.files[0]);
    }
  };

  const handleSummarize = async (type) => {
    if (!file) {
      alert("Please upload a book file first.");
      return;
    }

    const dummyResponse = {
      chapter: "Chapter 1: Introduction to Biology\nSummary: Biology is the study of living organisms...",
      topic: "Pages 10–15: Photosynthesis\nTopic Summary: This section explains how plants convert light into energy...",
      concept: "Book Concept: This book provides a comprehensive understanding of life sciences..."
    };

    switch (type) {
      case 'chapter':
        setSummary(dummyResponse.chapter);
        break;
      case 'topic':
        setTopicSummary(dummyResponse.topic);
        break;
      case 'concept':
        setBookConcept(dummyResponse.concept);
        break;
      default:
        break;
    }
  };

  return (
    <div className="p-8 max-w-4xl mx-auto space-y-6">
      <h1 className="text-3xl font-bold">📚 Book Summary Web App</h1>

      <Card>
        <CardContent className="p-4 space-y-4">
          <label className="font-semibold">Upload Book File (PDF, DOCX, etc):</label>
          <Input type="file" accept=".pdf,.doc,.docx" onChange={handleFileUpload} />

          <div className="flex flex-wrap gap-4">
            <Button onClick={() => handleSummarize('chapter')}>📖 Chapter Summary</Button>
            <Button onClick={() => handleSummarize('topic')}>📝 Topic Summary</Button>
            <Button onClick={() => handleSummarize('concept')}>💡 Book Concept</Button>
          </div>
        </CardContent>
      </Card>

      <Tabs defaultValue="chapter">
        <TabsList>
          <TabsTrigger value="chapter">Chapter Summary</TabsTrigger>
          <TabsTrigger value="topic">Topic Summary</TabsTrigger>
          <TabsTrigger value="concept">Book Concept</TabsTrigger>
        </TabsList>

        <TabsContent value="chapter">
          <Textarea value={summary} rows={10} readOnly className="mt-4" />
        </TabsContent>
        <TabsContent value="topic">
          <Textarea value={topicSummary} rows={10} readOnly className="mt-4" />
        </TabsContent>
        <TabsContent value="concept">
          <Textarea value={bookConcept} rows={10} readOnly className="mt-4" />
        </TabsContent>
      </Tabs>
    </div>
  );
}
